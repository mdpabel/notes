---
title: Object oriented programming (OOP)
description: Overview of Encapsulation, inheritance, polymorphism, and abstraction - and other topics.
date: 03-28-2024
status: published
priority: 1000
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact Information</title>
</head>
<body>

<table>
  <thead>
    <tr>
      <th>ENGINE</th>
      <th>Contact</th>
    </tr>
  </thead>
  <tbody id="contactTable">
  </tbody>
</table>

<script>
  // Array of objects containing contact information
  var contacts = [
    { engine: "Abusix", contact: "support@abusix.com" },
    { engine: "Abusix", contact: "https://lookup.abusix.com/" },
    // Add more objects here
  ];

  // Function to dynamically create table rows
  function populateTable() {
    var tableBody = document.getElementById("contactTable");
    for (var i = 0; i < contacts.length; i++) {
      var row = "<tr>";
      row += "<td>" + contacts[i].engine + "</td>";
      row += "<td>" + contacts[i].contact + "</td>";
      row += "</tr>";
      tableBody.innerHTML += row;
    }
  }

  // Call the function to populate the table
  populateTable();
</script>

</body>
</html>
