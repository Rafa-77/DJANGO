// ListGroup

// import ListGroup from "./components/ListGroup";

// function App() {
//   let items = ["New York", "San Francisco", "Tokio", "Paris"];
//   const handleSelectItem = (item: string) => {
//     console.log(item);
//   };
//   return (
//     <div>
//       <ListGroup
//         items={items}
//         heading={"Cities"}
//         onSelectItem={handleSelectItem}
//       />
//     </div>
//   );
// }

// export default App;

// Button
import { useState } from "react";
import Button from "./components/Button";
import Alert from "./components/Alert_button";

function App() {
  const [alertVisible, setAlertVisibility] = useState(false);

  return (
    <div>
      {alertVisible && (
        <Alert onClose={() => setAlertVisibility(false)}>My alert</Alert>
      )}
      <Button color="secondary" onClick={() => setAlertVisibility(true)}>
        Label-button01
      </Button>
    </div>
  );
}

export default App;
