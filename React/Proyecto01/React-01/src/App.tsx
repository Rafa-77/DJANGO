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
import Button from "./components/Button";

function App() {
  return (
    <div>
      <Button color="secondary" onClick={() => console.log("Clicled")}>
        Label
      </Button>
    </div>
  );
}

export default App;
