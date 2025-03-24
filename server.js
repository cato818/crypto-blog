// Elimiconst express = require("express");
const path = require("path");
const app = express();

// Sirve archivos estáticos de React en producción
if (process.env.NODE_ENV === "production") {
  app.use(express.static(path.join(__dirname, "build")));
  app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "build", "index.html"));
  });
}

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));nar este archivo ya que no será necesario sin Express.
