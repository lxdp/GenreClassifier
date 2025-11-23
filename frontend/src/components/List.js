import React from "react"

// 'export default' allows for reference to be made in other files
function List({items}) {
    return (
        <div className="song-grid">
        {/* Equivalent of for item in items */}
        {items.map((item) => (
            <div
            key={item.AudioName}
            className="song-card"
            onClick={() => console.log(item)}>
            <h4>{item.AudioName}</h4>
            <p>{item.Genre}</p>
            </div>
      ))}
    </div>
    )
}

export default List;