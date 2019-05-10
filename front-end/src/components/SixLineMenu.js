import React from 'react';
import '../index.css';

function SixLineMenu(props) {
    return (
        <div>
            <select class="custom-select" id="ominoe-select" onChange={props.setOminoeTypes} value={props.ominoe_id} width='200px'>
                <option value=""></option>
                <option value="pent-unq">Pentominoes (unique)</option>
                <option value="pent-non">Pentominoes (non-unique)</option>
                <option value="hex-non">Hexominoes (non-unique)</option>
                <option value="tetr-pent-non">Tetronimoes and Pentominoes (both non-unique)</option>
                <option value="tetr-unq-pent-non">Tetronimoes (unique) and Pentominoes (non-unique)</option>
                <option value="pent-hex-non">Pentominoes and Hexominoes (both non-unique)</option>
            </select>
            <button class="button" onClick={props.readyToTile}>Ready To Tile</button>
        </div>
    );
}

export default SixLineMenu;