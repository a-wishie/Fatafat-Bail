const express = require("express");
const { MongoClient } = require("mongodb");

const app = express();
const port = 3000;

app.use(express.json());

// MongoDB connection URL
const url = "mongodb://localhost:27017/Bail_Reckoner"; // Replace with your MongoDB connection URL
const dbName = "Bail_Reckoner"; // Replace with your database name

app.get("/documents", async (req, res) => {
  const columnValue = req.query.value; // Get the column value from query params

  if (!columnValue) {
    return res.status(400).json({ error: "Column value is required" });
  }

  const client = new MongoClient(url);

  try {
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection("Prisoners"); // Replace with your collection name

    // Find documents where the column matches the provided value
    const documents = await collection
      .find({ Prisoner_Id: columnValue })
      .toArray(); // Replace 'yourColumnName' with the actual column name

    res.json(documents);
  } catch (err) {
    res.status(500).json({ error: "An error occurred" });
  } finally {
    await client.close();
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
