<script>
var contacts = [
  { engine: "Abusix", contact: "support@abusix.com" },
  { engine: "Abusix", contact: "https://lookup.abusix.com/" },
  // Add more objects as needed
];

document.write("<table>");
document.write("<tr><th>ENGINE</th><th>Contact</th></tr>");
for (var i = 0; i < contacts.length; i++) {
  document.write("<tr>");
  document.write("<td>" + contacts[i].engine + "</td>");
  document.write("<td>" + contacts[i].contact + "</td>");
  document.write("</tr>");
}
document.write("</table>");
</script>
