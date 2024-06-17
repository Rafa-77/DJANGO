
function ListGroup() {
    let items = [
        "New York",
        "San Francisco",
        "Tokio",
        "Paris"
    ];

    items = [];
    
    const getMessage = () =>{
        return items.length === 0 && <p>No item found</p>
    }

    return (
        <>    
        <h1>List</h1>
        {getMessage() }
        <ul className="list-group">
            {items.map(item => (
                <li key = {item}>{item}</li>
                ))}
        </ul>
    </>
    );
}

export default ListGroup;
