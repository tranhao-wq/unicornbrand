import FallingText from './FallingText';
import './FallingText.css';

function App() {
  return (
    <div
      className="App"
      style={{
        background: 'transparent',
        minHeight: 'unset',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100vw',
        height: '180px',
        maxWidth: '1200px',
        margin: '0 auto',
      }}
    >
      <FallingText
        // --- Bắt đầu thay đổi ---
        text={`Unicorn Brand: Where every step is a magical journey. Discover our collection of stylish, comfortable, and enchanting footwear designed to make you shine.`}
        highlightWords={["Unicorn", "magical", "stylish", "shine"]}
        // --- Kết thúc thay đổi ---
        highlightClass="highlighted"
        trigger="hover"
        backgroundColor="transparent"
        wireframes={false}
        gravity={0.56}
        fontSize="3.5rem"
        mouseConstraintStiffness={0.9}
      />
    </div>
  );
}

export default App;