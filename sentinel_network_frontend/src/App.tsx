// import { useState } from "react";
import Login from "./screens/Login";
import ErrorMessage from "./components/ErrorMessage";
import Alert from "./components/Alert";

function App() {
  const msg = "Here is an alert!";

  return (
    <div className="container">
      <Alert color="primary" message={msg} />
    </div>
  );
}

export default App;
