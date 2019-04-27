import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import PoemInput from './components/PoemInput'
import SyllableCheck from './components/SyllableCheck'

class PuzzlePoem extends React.Component {
	render() {
		return (
			<div className="puzzle-poem">
				<div className="poem-input">
					<PoemInput />
				</div>
			</div>
		);
	}
}

// ========================================

ReactDOM.render(
	<PuzzlePoem />,
	document.getElementById('root')
);
