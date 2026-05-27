import Foundation

// MARK: - Analytics Models

struct DataPoint: Identifiable {
    let id = UUID()
    let date: Date
    let value: Double
}

struct MetricCategory: Identifiable {
    let id = UUID()
    let name: String
    let amount: Double
}

// MARK: - Research Models

struct ResearchTopic: Identifiable, Hashable {
    let id = UUID()
    let title: String
    let description: String
    let createdDate: Date
    let isFavorite: Bool
}

// MARK: - Data Manager

class DataManager: ObservableObject {
    @Published var dailyDataPoints: [DataPoint] = []
    @Published var categories: [MetricCategory] = []
    @Published var researchTopics: [ResearchTopic] = []

    init() {
        generateMockData()
    }

    private func generateMockData() {
        // Mock line chart data (e.g. daily active users or revenue)
        let calendar = Calendar.current
        var points: [DataPoint] = []
        let today = Date()
        for i in (0..<10).reversed() {
            if let date = calendar.date(byAdding: .day, value: -i, to: today) {
                let randomValue = Double.random(in: 100...500)
                points.append(DataPoint(date: date, value: randomValue))
            }
        }
        self.dailyDataPoints = points

        // Mock bar chart / category data
        self.categories = [
            MetricCategory(name: "Tech", amount: 1200),
            MetricCategory(name: "Health", amount: 850),
            MetricCategory(name: "Finance", amount: 1500),
            MetricCategory(name: "Education", amount: 620)
        ]

        // Mock research topics
        self.researchTopics = [
            ResearchTopic(title: "AI in Healthcare", description: "Analyzing the impact of predictive models in patient care.", createdDate: Date(), isFavorite: true),
            ResearchTopic(title: "Crypto Market Trends", description: "Quarterly review of decentralized finance growth.", createdDate: Date().addingTimeInterval(-86400 * 2), isFavorite: false),
            ResearchTopic(title: "Renewable Energy Adoption", description: "Global solar and wind adoption statistics for 2024.", createdDate: Date().addingTimeInterval(-86400 * 5), isFavorite: true),
            ResearchTopic(title: "Autonomous Vehicles", description: "Safety metrics and regulation analysis across top manufacturers.", createdDate: Date().addingTimeInterval(-86400 * 10), isFavorite: false)
        ]
    }
}
