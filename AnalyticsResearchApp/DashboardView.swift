import SwiftUI
import Charts

struct DashboardView: View {
    @EnvironmentObject var dataManager: DataManager

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {

                    // Daily Trends Line Chart
                    VStack(alignment: .leading) {
                        Text("Daily Activity Trends")
                            .font(.headline)

                        Chart(dataManager.dailyDataPoints) { point in
                            LineMark(
                                x: .value("Date", point.date),
                                y: .value("Value", point.value)
                            )
                            .symbol(Circle())
                            .interpolationMethod(.catmullRom)
                        }
                        .frame(height: 250)
                        .chartXAxis {
                            AxisMarks(values: .stride(by: .day)) { _ in
                                AxisGridLine()
                                AxisValueLabel(format: .dateTime.month().day())
                            }
                        }
                    }
                    .padding()
                    .background(Color.secondary.opacity(0.1))
                    .cornerRadius(12)

                    // Sector Analysis Bar Chart
                    VStack(alignment: .leading) {
                        Text("Investment by Sector")
                            .font(.headline)

                        Chart(dataManager.categories) { category in
                            BarMark(
                                x: .value("Category", category.name),
                                y: .value("Amount", category.amount)
                            )
                            .foregroundStyle(by: .value("Category", category.name))
                        }
                        .frame(height: 250)
                    }
                    .padding()
                    .background(Color.secondary.opacity(0.1))
                    .cornerRadius(12)

                }
                .padding()
            }
            .navigationTitle("Analytics Dashboard")
        }
    }
}

#Preview {
    DashboardView()
        .environmentObject(DataManager())
}
