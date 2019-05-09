import React from 'react';
import '../index.css';
import styled from 'styled-components'

const Input = styled.input`
    text-align: center;
    width: ${(props => props.num_words)}%;
    padding: 0.1em;
    margin: 0.1em;
`
const Wrapper = styled.span`
    display: table;
    width: 80%;
    table-layout: fixed;
`;

function PoemWord(props) {
    const word_id = "poem-word-".concat([props.outer_key, "-", props.inner_key])
    return (
        <Input num_words={props.word_count}
        type='text'
        id={word_id}
        onChange={() => props.onChange(props.outer_key, props.inner_key, word_id)}
        value={props.word}></Input>
    )
}

function PoemLine(props) {
    var syl_count = 0;
    var word_count = 0;
    for (var word in props.words) {
        var syl_list = props.words[word].trim().split(" ")
        syl_count += syl_list.length;
        word_count += 1;
    }
    let valid_line;

    word_count = 70 / word_count;

    if (syl_count === 10) {
        valid_line = ""
    } else {
        valid_line = "  Invalid: line must have 10 syllables"
    }
	return (
        <div>
            <Wrapper>
                {props.words.map((object, j) => 
                <PoemWord word={object} 
                key={j} 
                inner_key={j}
                outer_key={props.outer_key} 
                onChange={props.onChange}
                word_count={word_count}/>)}
                {valid_line}
            </Wrapper>
        </div>
	)
}

function PoemToCheck(props) {
    return (
        <div>
            {props.lines.map((object, i) => 
                <PoemLine words={object} 
                key={i} 
                outer_key={i}
                onChange={props.onChange}/>)}
        </div>
        )
}

export default PoemToCheck;