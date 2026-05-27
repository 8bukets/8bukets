import SwiftUI

@main
struct AnalyticsResearchApp: App {
    @StateObject private var dataManager = DataManager()

    var body: some Scene {
        WindowGroup {
            TabView {
                DashboardView()
                    .tabItem {
                        Label("Dashboard", systemName: "chart.line.uptrend.xyaxis")
                    }

                ResearchView()
                    .tabItem {
                        Label("Research", systemName: "doc.text.magnifyingglass")
                    }
            }
            .environmentObject(dataManager)
        }
    }
}
