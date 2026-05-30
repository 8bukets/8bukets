import SwiftUI

struct ResearchView: View {
    @EnvironmentObject var dataManager: DataManager
    @State private var searchText = ""

    var filteredTopics: [ResearchTopic] {
        if searchText.isEmpty {
            return dataManager.researchTopics
        } else {
            return dataManager.researchTopics.filter { $0.title.localizedCaseInsensitiveContains(searchText) || $0.description.localizedCaseInsensitiveContains(searchText) }
        }
    }

    var body: some View {
        NavigationStack {
            List(filteredTopics) { topic in
                NavigationLink(destination: ResearchDetailView(topic: topic)) {
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            Text(topic.title)
                                .font(.headline)
                            Spacer()
                            if topic.isFavorite {
                                Image(systemName: "star.fill")
                                    .foregroundColor(.yellow)
                            }
                        }
                        Text(topic.description)
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                            .lineLimit(2)
                    }
                    .padding(.vertical, 4)
                }
            }
            .navigationTitle("Research Hub")
            .searchable(text: $searchText, prompt: "Search topics...")
        }
    }
}

struct ResearchDetailView: View {
    let topic: ResearchTopic

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                Text(topic.title)
                    .font(.largeTitle)
                    .bold()

                HStack {
                    Text("Created on \(topic.createdDate, format: .dateTime.month().day().year())")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    Spacer()
                    if topic.isFavorite {
                        Label("Favorite", systemName: "star.fill")
                            .font(.caption)
                            .foregroundColor(.yellow)
                    }
                }

                Divider()

                Text(topic.description)
                    .font(.body)

                Spacer()
            }
            .padding()
        }
        .navigationTitle("Details")
        .navigationBarTitleDisplayMode(.inline)
    }
}

#Preview {
    ResearchView()
        .environmentObject(DataManager())
}
