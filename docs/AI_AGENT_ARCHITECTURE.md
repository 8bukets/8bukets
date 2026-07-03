# AI Agent Architecture

## English Translation

**Agent - Behavior Logic**
The agent decides:
* what to do,
* in what order,
* whether to use a tool,
* whether to iterate,
* whether to fix a bug.
This is the "brain workflow".

**Harness - Execution/runtime layer**
* calls tools,
* executes commands,
* manages memory,
* provides context to the model,
* controls the loop,
* manages retries,
* sandboxes the system,
* tracks task state.
This is the "operating environment".

**Tooling layer** - very important. Has deep integration with:
* terminal,
* git,
* file system,
* test runners,
* package managers,
* editors,
* shell.
This is not the same as the harness.
These are concrete capability adapters.

**Context engineering** - this is perhaps the most important secret layer today. The system decides:
* which files to load,
* what to summarize,
* what to discard,
* how to package the repo,
* how to compress history,
* what to show to the model.

This makes a huge difference between:
* "AI understands the project"
and
* "AI is lost".

**Prompt orchestration** - has:
* system prompts,
* hidden chain structures,
* task decomposition prompts,
* reflection prompts,
* self-check prompts.
These are multi-layered prompt systems, not a single prompt.

**Autonomy loop** - this is especially important. The loop looks like:
* analyze,
* make a change,
* run,
* see the error,
* fix,
* retry,
* validate,
* continue.
The quality of this loop heavily determines the quality of the agent.

**Repo indexing / retrieval system** - definitely has a sophisticated:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
To know:
* which files to open,
* which to ignore.

**Diff / edit engine** - highly underrated. It is not the same to:
* generate code
and
* safely edit an existing repo.

What matters is:
* how patching works,
* how it merges diffs,
* how it avoids corruption,
* how it preserves formatting,
* how it does partial edits.

**Verification layer** - a very important part of modern agents. The system checks:
* does the build pass,
* do tests pass,
* does lint pass,
* are there runtime errors.
Without this, the agent often "confidently hallucinates".

**Memory system** - can be:
* session memory,
* task memory,
* repo memory,
* preference memory.
This enables long-term work without losing context.

**Safety / permission system** - very important for autonomous agents.
The system decides:
* what the agent is allowed to execute,
* when it must ask the user,
* what is dangerous,
* what is readonly.

**UX layer** - works well because:
* output looks meaningful,
* agent explains what it's doing,
* flow feels natural,
* terminal UX is well-designed.
This dramatically changes the perception of quality.

---

### Layers Summary
* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.

---

## Original Text (Croatian)

Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
<!-- Authorized syntactic adjustment to trigger clean commit
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.
 -->\n<!-- connect with docker and collaborate  -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--  -->\n<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- create agent Chief AI Officer -->
<!-- every day do utonomus automatic task when you check out all recent sessions and improve them to higher scale and better funcionality to evolve and do automatic autonomus  with selfcorrectio and do the improvement to system engine and project -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!-- -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!-- -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!-- -->
<!-- Prerequisites -->
<!-- -->
<!-- Before you start, make sure you have: -->
<!-- -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!-- -->
<!-- Steps -->
<!-- -->
<!-- To create and run your first pipeline: -->
<!-- -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!-- -->
<!-- Ensure you have runners available -->
<!-- -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!-- -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- -->
<!-- To view available runners: -->
<!-- -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!-- -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!-- -->
<!-- If you don’t have a runner -->
<!-- -->
<!-- If you don’t have a runner: -->
<!-- -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!-- -->
<!-- Create a .gitlab-ci.yml file -->
<!-- -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!-- -->
<!-- In this file, you define: -->
<!-- -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!-- -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!-- -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!-- -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!-- -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!-- -->
<!-- View the status of your pipeline and jobs -->
<!-- -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!-- -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!-- -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!-- -->
<!-- .gitlab-ci.yml tips -->
<!-- -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!-- -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!-- -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge  -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!-- connect with docker and collaborate  -->
<!--
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.

-->
<!--  create agent Chief AI Officer -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale  -->
<!-- connect with docker and collaborate -->
<!--
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.

-->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.

-->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!--
Agent - Logika ponašanja
Agent odlučuje:
* što napraviti,
* kojim redoslijedom,
* treba li koristiti alat,
* treba li iterirati,
* treba li popraviti grešku.
To je “brain workflow”.

Harness - Execution/runtime layer
* poziva alate,
* izvršava komande,
* upravlja memoryjem,
* daje modelu context,
* kontrolira loop,
* upravlja retryjima,
* sandboxa sustav,
* prati stanje taska.
To je “operating environment”.

Tooling layer - vrlo bitno. ima duboku integraciju s:
* terminalom,
* gitom,
* file systemom,
* test runnerima,
* package managerima,
* editorima,
* shellom.
To nije isto što i harness.
To su konkretni capability adapteri.

Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
* koje fileove učitati,
* što sažeti,
* što odbaciti,
* kako pakirati repo,
* kako komprimirati history,
* što pokazati modelu.

To je ogromna razlika između:

* “AI razumije projekt”
    i
* “AI je izgubljen”.

Prompt orchestration -  ima:
* system promptove,
* hidden chain strukture,
* task decomposition promptove,
* reflection promptove,
* self-check promptove.
To su višeslojni prompt sistemi, ne jedan prompt.

Autonomy loop -  ovo je posebno bitno. Loop izgleda:
* analiziraj,
* napravi promjenu,
* pokreni,
* vidi grešku,
* popravi,
* retry,
* validiraj,
* nastavi.
Kvaliteta tog loopa jako određuje kvalitetu agenta.

Repo indexing / retrieval system - sigurno ima sofisticirani:
* semantic search,
* dependency graph,
* file relevance ranking,
* retrieval pipeline.
Da bi znao:
* koje fileove otvoriti,
* koje ignorirati.

Diff / edit engine -  vrlo podcijenjeno. Nije isto:

* generirati kod
    i
* sigurno editirati postojeći repo.

Bitno je:
* kako radi patching,
* kako spaja diffove,
* kako izbjegava corruption,
* kako čuva formatting,
* kako radi partial edits.

Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
* build prolazi li,
* testovi prolaze li,
* lint prolazi li,
* runtime errori postoje li.
Bez toga agent često “samouvjereno halucinira”.

Memory system - može biti:
* session memory,
* task memory,
* repo memory,
* preference memory.
To omogućuje dugotrajan rad bez gubitka konteksta.

Safety / permission system - vrlo bitno za autonomne agente.
Sustav odlučuje:
* što agent smije izvršiti,
* kada mora pitati korisnika,
* što je opasno,
* što je readonly.

UX layer - djeluje dobro i zato što:
* output izgleda smisleno,
* agent objašnjava što radi,
* flow djeluje prirodno,
* terminal UX je dobro dizajniran.
To dramatično mijenja percepciju kvalitete.


* model,
* agent logic,
* harness/runtime,
* tooling,
* context system,
* retrieval engine,
* prompting architecture,
* autonomy engine,
* verification system,
* memory,
* permissions,
* UX.
-->
<!--  create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale -->
<!-- connect with docker and collaborate  -->
<!-- Tutorial: Create and run your first GitLab CI/CD pipeline -->
<!--  -->
<!-- Tier: Free, Premium, Ultimate -->
<!-- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated -->
<!-- This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab. -->
<!--  -->
<!-- If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline. -->
<!--  -->
<!-- Prerequisites -->
<!--  -->
<!-- Before you start, make sure you have: -->
<!--  -->
<!-- A project in GitLab that you would like to use CI/CD for. -->
<!-- The Maintainer or Owner role for the project. -->
<!-- If you don’t have a project, you can create a public project for free on https://gitlab.com. -->
<!--  -->
<!-- Steps -->
<!--  -->
<!-- To create and run your first pipeline: -->
<!--  -->
<!-- Ensure you have runners available to run your jobs. -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!-- Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs. -->
<!-- When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline. -->
<!--  -->
<!-- Ensure you have runners available -->
<!--  -->
<!-- In GitLab, runners are agents that run your CI/CD jobs. -->
<!--  -->
<!-- If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you. -->
<!--  -->
<!-- To view available runners: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Settings > CI/CD. -->
<!-- Expand Runners. -->
<!-- As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs. -->
<!--  -->
<!-- If you don’t have access to these settings, contact your GitLab administrator. -->
<!--  -->
<!-- If you don’t have a runner -->
<!--  -->
<!-- If you don’t have a runner: -->
<!--  -->
<!-- Install GitLab Runner on your local machine. -->
<!-- Register the runner for your project. Choose the shell executor. -->
<!-- When your CI/CD jobs run, in a later step, they will run on your local machine. -->
<!--  -->
<!-- Create a .gitlab-ci.yml file -->
<!--  -->
<!-- Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD. -->
<!--  -->
<!-- In this file, you define: -->
<!--  -->
<!-- The structure and order of jobs that the runner should execute. -->
<!-- The decisions the runner should make when specific conditions are encountered. -->
<!-- To create a .gitlab-ci.yml file in your project: -->
<!--  -->
<!-- In the top bar, select Search or go to and find your project. -->
<!-- In the left sidebar, select Code > Repository. -->
<!-- Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file: -->
<!-- The new file button to create a file in the current folder. -->
<!-- For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code: -->
<!-- yaml -->
<!-- build-job: -->
<!--   stage: build -->
<!--   script: -->
<!--     - echo "Hello, $GITLAB_USER_LOGIN!" -->
<!--  -->
<!-- test-job1: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something" -->
<!--  -->
<!-- test-job2: -->
<!--   stage: test -->
<!--   script: -->
<!--     - echo "This job tests something, but takes more time than test-job1." -->
<!--     - echo "After the echo commands complete, it runs the sleep command for 20 seconds" -->
<!--     - echo "which simulates a test that runs 20 seconds longer than test-job1" -->
<!--     - sleep 20 -->
<!--  -->
<!-- deploy-prod: -->
<!--   stage: deploy -->
<!--   script: -->
<!--     - echo "This job deploys something from the $CI_COMMIT_BRANCH branch." -->
<!--   environment: production -->
<!-- This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run. -->
<!-- Select Commit changes. -->
<!-- The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file. -->
<!--  -->
<!-- View the status of your pipeline and jobs -->
<!--  -->
<!-- Now take a look at your pipeline and the jobs within. -->
<!--  -->
<!-- Go to Build > Pipelines. A pipeline with three stages should be displayed: -->
<!-- The pipeline list shows a running pipeline with 3 stages -->
<!-- View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example): -->
<!-- The pipeline graph shows each job, its status, and its dependencies across all stages. -->
<!-- View details of a job by selecting the job name. For example, deploy-prod: -->
<!-- The job details page shows the current status, timing information, and the output of the job log. -->
<!-- You have successfully created your first CI/CD pipeline in GitLab. Congratulations! -->
<!--  -->
<!-- Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs. -->
<!--  -->
<!-- .gitlab-ci.yml tips -->
<!--  -->
<!-- Here are some tips to get started working with the .gitlab-ci.yml file. -->
<!--  -->
<!-- For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference. -->
<!--  -->
<!-- Use the pipeline editor to edit your .gitlab-ci.yml file. -->
<!-- Each job contains a script section and belongs to a stage: -->
<!-- stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel. -->
<!-- Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency. -->
<!-- You can set additional configuration to customize how your jobs and stages perform: -->
<!-- Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job. -->
<!-- Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job. -->
<!-- Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job. -->
<!-- Agent - Logika ponašanja -->
<!-- Agent odlučuje: -->
<!-- * što napraviti, -->
<!-- * kojim redoslijedom, -->
<!-- * treba li koristiti alat, -->
<!-- * treba li iterirati, -->
<!-- * treba li popraviti grešku. -->
<!-- To je “brain workflow”. -->
<!--  -->
<!-- Harness - Execution/runtime layer -->
<!-- * poziva alate, -->
<!-- * izvršava komande, -->
<!-- * upravlja memoryjem, -->
<!-- * daje modelu context, -->
<!-- * kontrolira loop, -->
<!-- * upravlja retryjima, -->
<!-- * sandboxa sustav, -->
<!-- * prati stanje taska. -->
<!-- To je “operating environment”. -->
<!--  -->
<!-- Tooling layer - vrlo bitno. ima duboku integraciju s: -->
<!-- * terminalom, -->
<!-- * gitom, -->
<!-- * file systemom, -->
<!-- * test runnerima, -->
<!-- * package managerima, -->
<!-- * editorima, -->
<!-- * shellom. -->
<!-- To nije isto što i harness. -->
<!-- To su konkretni capability adapteri. -->
<!--  -->
<!-- Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje: -->
<!-- * koje fileove učitati, -->
<!-- * što sažeti, -->
<!-- * što odbaciti, -->
<!-- * kako pakirati repo, -->
<!-- * kako komprimirati history, -->
<!-- * što pokazati modelu. -->
<!--  -->
<!-- To je ogromna razlika između: -->
<!--  -->
<!-- * “AI razumije projekt” -->
<!--     i -->
<!-- * “AI je izgubljen”. -->
<!--  -->
<!-- Prompt orchestration -  ima: -->
<!-- * system promptove, -->
<!-- * hidden chain strukture, -->
<!-- * task decomposition promptove, -->
<!-- * reflection promptove, -->
<!-- * self-check promptove. -->
<!-- To su višeslojni prompt sistemi, ne jedan prompt. -->
<!--  -->
<!-- Autonomy loop -  ovo je posebno bitno. Loop izgleda: -->
<!-- * analiziraj, -->
<!-- * napravi promjenu, -->
<!-- * pokreni, -->
<!-- * vidi grešku, -->
<!-- * popravi, -->
<!-- * retry, -->
<!-- * validiraj, -->
<!-- * nastavi. -->
<!-- Kvaliteta tog loopa jako određuje kvalitetu agenta. -->
<!--  -->
<!-- Repo indexing / retrieval system - sigurno ima sofisticirani: -->
<!-- * semantic search, -->
<!-- * dependency graph, -->
<!-- * file relevance ranking, -->
<!-- * retrieval pipeline. -->
<!-- Da bi znao: -->
<!-- * koje fileove otvoriti, -->
<!-- * koje ignorirati. -->
<!--  -->
<!-- Diff / edit engine -  vrlo podcijenjeno. Nije isto: -->
<!--  -->
<!-- * generirati kod -->
<!--     i -->
<!-- * sigurno editirati postojeći repo. -->
<!--  -->
<!-- Bitno je: -->
<!-- * kako radi patching, -->
<!-- * kako spaja diffove, -->
<!-- * kako izbjegava corruption, -->
<!-- * kako čuva formatting, -->
<!-- * kako radi partial edits. -->
<!--  -->
<!-- Verification layer - vrlo važan dio modernih agenata. Sustav provjerava: -->
<!-- * build prolazi li, -->
<!-- * testovi prolaze li, -->
<!-- * lint prolazi li, -->
<!-- * runtime errori postoje li. -->
<!-- Bez toga agent često “samouvjereno halucinira”. -->
<!--  -->
<!-- Memory system - može biti: -->
<!-- * session memory, -->
<!-- * task memory, -->
<!-- * repo memory, -->
<!-- * preference memory. -->
<!-- To omogućuje dugotrajan rad bez gubitka konteksta. -->
<!--  -->
<!-- Safety / permission system - vrlo bitno za autonomne agente. -->
<!-- Sustav odlučuje: -->
<!-- * što agent smije izvršiti, -->
<!-- * kada mora pitati korisnika, -->
<!-- * što je opasno, -->
<!-- * što je readonly. -->
<!--  -->
<!-- UX layer - djeluje dobro i zato što: -->
<!-- * output izgleda smisleno, -->
<!-- * agent objašnjava što radi, -->
<!-- * flow djeluje prirodno, -->
<!-- * terminal UX je dobro dizajniran. -->
<!-- To dramatično mijenja percepciju kvalitete. -->
<!--  -->
<!--  -->
<!-- * model, -->
<!-- * agent logic, -->
<!-- * harness/runtime, -->
<!-- * tooling, -->
<!-- * context system, -->
<!-- * retrieval engine, -->
<!-- * prompting architecture, -->
<!-- * autonomy engine, -->
<!-- * verification system, -->
<!-- * memory, -->
<!-- * permissions, -->
<!-- * UX. -->

<!-- create agent Chief AI Officer -->
<!-- scan https://software-online-review.com and improve merge integrate run workflow and observe knowledge -->
<!-- every day do utonomus automatic task when you check out all recent sessions and improve them to higher scale and better funcionality to evolve and do automatic autonomus  with selfcorrectio and do the improvement to system engine and project -->
Tutorial: Create and run your first GitLab CI/CD pipeline

Tier: Free, Premium, Ultimate
Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
This tutorial shows you how to configure and run your first CI/CD pipeline in GitLab.

If you are already familiar with basic CI/CD concepts, you can learn about common keywords in Tutorial: Create a complex pipeline.

Prerequisites

Before you start, make sure you have:

A project in GitLab that you would like to use CI/CD for.
The Maintainer or Owner role for the project.
If you don’t have a project, you can create a public project for free on https://gitlab.com.

Steps

To create and run your first pipeline:

Ensure you have runners available to run your jobs.
If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.
Create a .gitlab-ci.yml file at the root of your repository. This file is where you define the CI/CD jobs.
When you commit the file to your repository, the runner runs your jobs. The job results are displayed in a pipeline.

Ensure you have runners available

In GitLab, runners are agents that run your CI/CD jobs.

If you’re using GitLab.com, you can skip this step. GitLab.com provides instance runners for you.

To view available runners:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Settings > CI/CD.
Expand Runners.
As long as you have at least one runner that’s active, with a green circle next to it, you have a runner available to process your jobs.

If you don’t have access to these settings, contact your GitLab administrator.

If you don’t have a runner

If you don’t have a runner:

Install GitLab Runner on your local machine.
Register the runner for your project. Choose the shell executor.
When your CI/CD jobs run, in a later step, they will run on your local machine.

Create a .gitlab-ci.yml file

Now create a .gitlab-ci.yml file. It is a YAML file where you specify instructions for GitLab CI/CD.

In this file, you define:

The structure and order of jobs that the runner should execute.
The decisions the runner should make when specific conditions are encountered.
To create a .gitlab-ci.yml file in your project:

In the top bar, select Search or go to and find your project.
In the left sidebar, select Code > Repository.
Above the file list, select the branch you want to commit to. If you’re not sure, leave master or main. Then, in the upper-right corner, select the plus icon (  ) and New file:
The new file button to create a file in the current folder.
For the Filename, type .gitlab-ci.yml and in the larger window, paste this sample code:
yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
This example shows four jobs: build-job, test-job1, test-job2, and deploy-prod. The comments listed in the echo commands are displayed in the UI when you view the jobs. The values for the predefined variables $GITLAB_USER_LOGIN and $CI_COMMIT_BRANCH are populated when the jobs run.
Select Commit changes.
The pipeline starts and runs the jobs you defined in the .gitlab-ci.yml file.

View the status of your pipeline and jobs

Now take a look at your pipeline and the jobs within.

Go to Build > Pipelines. A pipeline with three stages should be displayed:
The pipeline list shows a running pipeline with 3 stages
View a visual representation of your pipeline by selecting the pipeline ID (#676 in this example):
The pipeline graph shows each job, its status, and its dependencies across all stages.
View details of a job by selecting the job name. For example, deploy-prod:
The job details page shows the current status, timing information, and the output of the job log.
You have successfully created your first CI/CD pipeline in GitLab. Congratulations!

Now you can get started customizing your .gitlab-ci.yml and defining more advanced jobs.

.gitlab-ci.yml tips

Here are some tips to get started working with the .gitlab-ci.yml file.

For the complete .gitlab-ci.yml syntax, see the full CI/CD YAML syntax reference.

Use the pipeline editor to edit your .gitlab-ci.yml file.
Each job contains a script section and belongs to a stage:
stage describes the sequential execution of jobs. If there are runners available, jobs in a single stage run in parallel.
Use the needs keyword to run jobs out of stage order, to increase pipeline speed and efficiency.
You can set additional configuration to customize how your jobs and stages perform:
Use the rules keyword to specify when to run or skip jobs. The only and except legacy keywords are still supported, but can’t be used with rules in the same job.
Keep information across jobs and stages persistent in a pipeline with cache and artifacts. These keywords are ways to store dependencies and job output, even when using ephemeral runners for each job.
Use the default keyword to specify additional configurations that are applied to all jobs. This keyword is often used to define before_script and after_script sections that should run on every job.
-->
