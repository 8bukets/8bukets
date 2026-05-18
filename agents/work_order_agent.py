import json
import os
import asyncio
from datetime import datetime
from .base_agent import BaseAgent, Blackboard

WORK_ORDERS_FILE = "data/work_orders.json"

class WorkOrderAgent(BaseAgent):
    """
    Work Order Agent: Manages the 'Creation Order' and 'Execution Queue' for autonomous tasks.
    It identifies necessary work (e.g., content creation, deployment steps, research tasks)
    and tracks their completion state.
    """
    def __init__(self):
        super().__init__("WorkOrderAgent",
                         dependencies=["system_evolution", "antigravity_context", "research_data"],
                         provides=["work_order_status", "creation_queue"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Managing Autonomous Work Orders and Creation Queue...")

        # 1. Load existing work orders
        orders = self._load_work_orders()

        # 2. Analyze system state to identify new work
        evolution = blackboard.get("system_evolution", {})
        antigravity = blackboard.get("antigravity_context", {})
        research = blackboard.get("research_data", {})

        new_tasks_identified = []

        # Scenario: If system evolved, we need a deployment order and a smoke test
        if evolution.get("status") == "EVOLVED":
            version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")

            # Deployment Task
            deploy_task_id = f"DEPLOY_V{version}"
            if not self._order_exists(orders, deploy_task_id):
                new_tasks_identified.append({
                    "id": deploy_task_id,
                    "type": "DEPLOYMENT",
                    "description": f"Execute rollout for version {version}",
                    "status": "pending",
                    "created_at": datetime.now().isoformat()
                })

            # Smoke Test Task
            smoke_task_id = f"SMOKE_TEST_V{version}"
            if not self._order_exists(orders, smoke_task_id):
                new_tasks_identified.append({
                    "id": smoke_task_id,
                    "type": "TESTING",
                    "description": f"Verify system stability for version {version}",
                    "status": "pending",
                    "created_at": datetime.now().isoformat()
                })

        # Scenario: Content Creation based on Market Trends
        market_trends = research.get("market_trends", [])
        if market_trends:
            # Create content for ALL major trends found (expanded from top 2)
            for trend in market_trends:
                task_id = f"CONTENT_{trend.replace(' ', '_').replace('.', '').upper()}"
                if not self._order_exists(orders, task_id):
                    new_tasks_identified.append({
                        "id": task_id,
                        "type": "CONTENT_CREATION",
                        "description": f"Generate structured review/content for trend: {trend}",
                        "status": "pending",
                        "created_at": datetime.now().isoformat()
                    })

        # Scenario: Proactive Investigation for Restricted/Unreachable Domains
        investigations = research.get("external_investigations", [])
        for inv in investigations:
            if inv.get("status") in ["RESTRICTED", "UNREACHABLE"]:
                domain = inv.get("domain")
                task_id = f"INVESTIGATE_{domain.replace('.', '_').upper()}"
                if not self._order_exists(orders, task_id):
                    new_tasks_identified.append({
                        "id": task_id,
                        "type": "RESEARCH",
                        "description": f"Deep investigation of connectivity issues for domain: {domain}",
                        "status": "pending",
                        "created_at": datetime.now().isoformat()
                    })

        # Scenario: Ensure market research is refreshed periodically
        if not self._order_exists(orders, "REFRESH_MARKET_INTELLIGENCE"):
             new_tasks_identified.append({
                    "id": "REFRESH_MARKET_INTELLIGENCE",
                    "type": "RESEARCH",
                    "description": "Perform deep scrape of market trends",
                    "status": "pending",
                    "created_at": datetime.now().isoformat()
                })

        # Scenario: Identify missing technical documentation
        tech_docs = ["JULES_CLI.md", "JULES_TOOLS.md", "SYSTEM_PATENT.md"]
        for doc in tech_docs:
            if not os.path.exists(doc):
                task_id = f"GENERATE_{doc.replace('.', '_').upper()}"
                if not self._order_exists(orders, task_id):
                    new_tasks_identified.append({
                        "id": task_id,
                        "type": "CONTENT_CREATION",
                        "description": f"Generate missing technical documentation: {doc}",
                        "status": "pending",
                        "created_at": datetime.now().isoformat()
                    })

        # Scenario: Identify STALE_DOCUMENTATION
        intel_report = "CONSOLIDATED_INTELLIGENCE.md"
        if os.path.exists(intel_report):
            mtime = os.path.getmtime(intel_report)
            if (datetime.now().timestamp() - mtime) > 86400: # 24 hours
                task_id = "REFRESH_INTELLIGENCE"
                if not self._order_exists(orders, task_id):
                    new_tasks_identified.append({
                        "id": task_id,
                        "type": "RESEARCH",
                        "description": "Refresh consolidated system intelligence",
                        "status": "pending",
                        "created_at": datetime.now().isoformat()
                    })

        # 3. Update orders and save
        if new_tasks_identified:
            for task in new_tasks_identified:
                self.logger.info(f"New Work Order Created: {task['id']}")
                orders.append(task)
            self._save_work_orders(orders)

        # 4. Refine Status Transitioning
        # Identify tasks that can be picked up immediately
        for o in orders:
            if o["status"] == "pending":
                # Simulated pick-up: if it's a research task, we might mark it as in progress
                if o["type"] == "RESEARCH":
                    o["status"] = "in_progress"
                    o["updated_at"] = datetime.now().isoformat()

        self._save_work_orders(orders)

        # 5. Prepare provides
        pending_count = len([o for o in orders if o["status"] == "pending"])
        in_progress_count = len([o for o in orders if o["status"] == "in_progress"])
        completed_count = len([o for o in orders if o["status"] == "completed"])

        status = {
            "pending_orders": pending_count,
            "in_progress_orders": in_progress_count,
            "completed_orders": completed_count,
            "last_order_id": orders[-1]["id"] if orders else None,
            "system_readiness": "OPTIMAL" if pending_count < 10 else "BUSY"
        }

        return {
            "work_order_status": status,
            "creation_queue": [o for o in orders if o["status"] != "completed"]
        }

    def _load_work_orders(self) -> list:
        if not os.path.exists(WORK_ORDERS_FILE):
            return []
        try:
            with open(WORK_ORDERS_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load work orders: {e}")
            return []

    def _save_work_orders(self, orders: list):
        try:
            os.makedirs(os.path.dirname(WORK_ORDERS_FILE), exist_ok=True)
            with open(WORK_ORDERS_FILE, 'w') as f:
                json.dump(orders, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save work orders: {e}")

    def _order_exists(self, orders: list, order_id: str) -> bool:
        return any(o["id"] == order_id for o in orders)

    async def review(self, blackboard: Blackboard):
        status = blackboard.get("work_order_status", {})
        if status.get("pending_orders", 0) > 20:
            return ["WARNING: High volume of pending work orders. Scaling might be required."]
        return ["Work order queue is under control."]
