import SwiftUI

struct Activity: Codable, Identifiable {
    var id = UUID()
    var activity: String
    var start_time: String
    var end_time: String
}

struct ContentView: View {
    @State private var activities = [Activity]()
    @State private var activityName = ""
    @State private var startTime = ""
    @State private var endTime = ""
    
    var body: some View {
        VStack {
            Text("Day Planner")
                .font(.largeTitle)
                .padding()
            
            // Input for activity
            TextField("Activity Name", text: $activityName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // Input for start time
            TextField("Start Time (HH:MM)", text: $startTime)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // Input for end time
            TextField("End Time (HH:MM)", text: $endTime)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // Add activity button
            Button(action: {
                addActivity()
            }) {
                Text("Add Activity")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            .padding()
            
            // List of activities
            List(activities) { activity in
                Text("\(activity.start_time) - \(activity.end_time): \(activity.activity)")
            }
        }
        .onAppear(perform: loadActivities)
    }
    
    // Function to add an activity
    func addActivity() {
        let newActivity = Activity(activity: activityName, start_time: startTime, end_time: endTime)
        
        // Prepare URL and request
        guard let url = URL(string: "http://localhost:3000/activities") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // Encode the activity to JSON
        guard let activityData = try? JSONEncoder().encode(newActivity) else { return }
        request.httpBody = activityData
        
        // Perform the request
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error adding activity: \(error.localizedDescription)")
                return
            }
            loadActivities() // Refresh activities after adding
        }.resume()
        
        // Clear input fields
        activityName = ""
        startTime = ""
        endTime = ""
    }
    
    // Function to load activities from the backend
    func loadActivities() {
        guard let url = URL(string: "http://localhost:3000/activities") else { return }
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            if let data = data {
                if let decodedActivities = try? JSONDecoder().decode([Activity].self, from: data) {
                    DispatchQueue.main.async {
                        self.activities = decodedActivities
                    }
                }
            }
        }.resume()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}