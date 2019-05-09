import React from 'react';
import '../index.css';
import styled from 'styled-components'

const TD = styled.td`
    text-align: center;
    border-top: ${(props => props.top)}px solid black;
    border-bottom: ${(props => props.bottom)}px solid black;
    border-right: ${(props => props.right)}px solid black;
    border-left: ${(props => props.left)}px solid black;
    height: 50px;
    width: 50px;    
`
///border-width: ${(props => props.top)}px ${(props => props.right)}px ${(props => props.bottom)}px ${(props => props.left)}px;
function TableRow(props) {
    console.log(props.syllables[0])
    return(
        <tr>
            {props.syllables.map((object, i) => 
            <TD key={i} top={object.top} right={object.right} bottom={object.bottom} left={object.left}>
                {object.text}
            </TD>)}
        </tr>
    )
}

function PuzzleDisplay(props) {
    var syllable_poem = props.syllable_poem;
    var tiled_poem = props.tiled_poem;

    var flattened_syls = []
    for (var i in syllable_poem) {
        var line = syllable_poem[i]
        for (var j in line) {
            var word = line[j]
            var syllables = word.trim().split(" ")
            for (var k in syllables) {
                var syllable = syllables[k];
                var tileSquare = {'text': syllable, 'top': 0, 'right': 0, 'bottom': 0, 'left': 0}
                flattened_syls.push(tileSquare)
            }
        }
    }

    var num_syls = flattened_syls.length
    var syl_count = 0

    for (var i in flattened_syls) {
        syl_count = syl_count + 1;

        i = parseInt(i)
        for (var tiled_i in tiled_poem) {
            var piece = tiled_poem[tiled_i]
            if (piece.includes(i)) {
                if (!piece.includes(i-1)) {
                    // left border
                    flattened_syls[i].left = 1
                }
                if (!piece.includes(i+1)) {
                    // right border
                    flattened_syls[i].right = 1
                }
                if (!piece.includes(i-10)) {
                    // top border
                    flattened_syls[i].top = 1
                }
                if (!piece.includes(i+10)) {
                    // bottom border
                    flattened_syls[i].bottom = 1
                }
                break;
            }
        }
    }

    // unflatten array
    var curr_index = 0
    var lines = (num_syls) / 10
    var tiled_syllable_poem = []

    for (var i = 0; i < lines; i++) {
        var new_line = []
        for (var j = 0; j < 10; j++) {
            new_line.push(flattened_syls[curr_index])
            curr_index += 1;
        }
        tiled_syllable_poem.push(new_line)
    }

    return (
        <table cellSpacing="0">
            <tbody>
                {tiled_syllable_poem.map((object, i) =>
                <TableRow key={i}
                syllables={object}/>)}
            </tbody>
        </table>
    );
}

export default PuzzleDisplay;