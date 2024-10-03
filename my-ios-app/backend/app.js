const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.json()); // Middleware to parse JSON

let todo_list = [];

// Load existing todo_list from JSON file (if exists)
if (fs.existsSync('todo_list.json')) {
    todo_list = JSON.parse(fs.readFileSync('todo_list.json'));
}

// Get all activities
app.get('/activities', (req, res) => {
    res.json(todo_list);
});

// Add a new activity
app.post('/activities', (req, res) => {
    const { activity, start_time, end_time } = req.body;

    if (!activity || !start_time || !end_time) {
        return res.status(400).json({ error: "Missing activity, start_time or end_time" });
    }

    todo_list.push({ activity, start_time, end_time });
    todo_list.sort((a, b) => new Date(`1970-01-01T${a.start_time}`) - new Date(`1970-01-01T${b.start_time}`));

    // Save to JSON file
    fs.writeFileSync('todo_list.json', JSON.stringify(todo_list));

    res.status(201).json({ message: "Activity added", todo_list });
});

// Start server
app.listen(port, () => {
    console.log(`Backend server running at http://localhost:${port}`);
});