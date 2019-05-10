import React from 'react';
import '../index.css';
import styled from 'styled-components'
import AllPuzzles from './PuzzleDisplay'
import PoemToCheck from './SyllableCheck'
import EightLineMenu from './EightLineMenu'
import SixLineMenu from './SixLineMenu'

var api_url = "http://localhost:5000"

class PoemInput extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
            poem_text: "",
            poem_lines: [],
            ready_to_check: false,
            syllable_poem: [],
            ominoe_types: [],
            unique_types: [],
            ominoe_id: "",
            num_tilings: 1,
            ready_to_tile: false,
            tiled_poem: null,
            enter_new_poem: true,
            waiting_for_tiling: false,
        }
        this.handlePoemEdit = this.handlePoemEdit.bind(this);
        this.setPoem = this.setPoem.bind(this);
        this.readyToCheck = this.readyToCheck.bind(this);
        this.setSyllablePoem = this.readyToCheck.bind(this);
        this.setOminoeTypes = this.setOminoeTypes.bind(this);
        this.readyToTile = this.readyToTile.bind(this);
        this.setTiledPoem = this.setTiledPoem.bind(this);
        this.editPoem = this.editPoem.bind(this);
        this.returnToCheck = this.returnToCheck.bind(this);
    }

    setPoem() {
        this.setState({
            poem_text: document.getElementById("poem_text").value,
        })
    }

    readyToCheck() {
        var poem_lines = this.state.poem_text.split("\n");
        var poem_lines_processed = [];
        for (var i in poem_lines) {
            var line = poem_lines[i].trim();
            if (line !== "") {
                poem_lines_processed.push(line)
            }
        }

        var ready_to_check = false;
        if (poem_lines_processed.length === 6 || poem_lines_processed.length === 8) {
            ready_to_check = true;
        } else {
            window.alert("Please enter either 6 or 8 lines.")
        }

        var syllable_poem = [];
        if (ready_to_check) {
            var request_string = ""
            for (var line in poem_lines_processed) {
                request_string = request_string.concat("/");
                request_string = request_string.concat(poem_lines_processed[line])
            }

		        var fetch_url = api_url.concat("/api/poem-syllable?poem=")
            fetch_url = fetch_url.concat(request_string);

            var that = this;
            fetch(fetch_url).then(function(response) {
                return response.json();
            }).then(function(json) {
                syllable_poem = json.data;
                that.setState({
                    ready_to_check: true,
                    enter_new_poem: false,
                    poem_lines: poem_lines_processed,
                    syllable_poem: syllable_poem,
                })
                return json;
            });
        } else {
            this.setState({
                ready_to_check: false,
                enter_new_poem: true,
                poem_lines: poem_lines_processed,
            })
        }
    }

    handlePoemEdit(i, j, word_id) {
        const syllable_poem = this.state.syllable_poem.slice();
        syllable_poem[i][j] = document.getElementById(word_id).value;
        this.setState({
           syllable_poem: syllable_poem
        })
    }

    setSyllablePoem(syllable_poem) {
        this.setState({
            syllable_poem: syllable_poem,
        })
    }

    setOminoeTypes() {
        var ominoe_type_dict = {"pent-non": [[5], [0]],
                    "tetr-pent-unq": [[4, 5], [1, 1]],
                    "tetr-pent-non": [[4, 5], [0, 0]],
                    "tetr-unq-pent-non": [[4, 5], [1, 0]],
                    "tetr-non-pent-unq": [[4, 5], [0, 1]],
                    "pent-hex-non": [[5, 6], [0, 0]],
                    // these vals only used for 6-line
                    "pent-unq": [[5],[1]],
                    "hex-non": [[6],[0]]};

        var ominoe_type_id = document.getElementById("ominoe-select").value;
        var ominoe_types = [];
        var unique_types = [];

        if (ominoe_type_id in ominoe_type_dict) {
            ominoe_types = ominoe_type_dict[ominoe_type_id][0];
            unique_types = ominoe_type_dict[ominoe_type_id][1];
        }

        console.log(ominoe_types)

        this.setState({
            ominoe_types: ominoe_types,
            unique_types: unique_types,
            ominoe_id: ominoe_type_id,
        })
    }

    readyToTile() {
        // check if ominoe type has been selected
        var alert_text = '';

        var ominoe_type_selected = false;
        if (this.state.ominoe_types.length > 0 && this.state.ominoe_types.length === this.state.unique_types.length) {
            ominoe_type_selected = true;
        } else {
            alert_text = "Error: must select ominoe type"
        }

        var num_tilings_selected = false;
        if (this.state.num_tilings > 0) {
            num_tilings_selected = true;
        } else {
            alert_text = alert_text.concat('\nError: must enter non-zero tiling number')
        }

        // check if all lines have 10 syllables
        var correct_syllables = true;
        for (var line_index in this.state.syllable_poem) {
            var line = this.state.syllable_poem[line_index]
            var syl_count = 0;
            for (var word in line) {
                var syl_list = line[word].trim().split(" ")
                syl_count += syl_list.length;
            }
            if (syl_count !== 10) {
                correct_syllables = false;
            }
        }

        if (!correct_syllables) {
            alert_text = alert_text.concat("\nError: all lines must contain exactly 10 syllables")
        }

        var ready_to_tile = ominoe_type_selected && num_tilings_selected && correct_syllables;
        if (!ready_to_tile) {
            window.alert(alert_text)
        }

        if (ready_to_tile) {
            //TODO: send correct info to api
            var fetch_url = api_url.concat("/api/puzzle?")

            fetch_url = fetch_url.concat("syllable_poem=");
            fetch_url = fetch_url.concat(this.state.syllable_poem.toString());

            fetch_url = fetch_url.concat("&num_tilings=");
            fetch_url = fetch_url.concat(this.state.num_tilings)

            var poem_size = this.state.poem_lines.length * 10;
            fetch_url = fetch_url.concat("&poem_size=");
            fetch_url = fetch_url.concat(poem_size);

            fetch_url = fetch_url.concat("&num_ominoe_sizes=");
            fetch_url = fetch_url.concat(this.state.ominoe_types.length);

            fetch_url = fetch_url.concat("&ominoe_sizes=");
            fetch_url = fetch_url.concat(this.state.ominoe_types.toString());

            fetch_url = fetch_url.concat("&unq_ominoes=");
            fetch_url = fetch_url.concat(this.state.unique_types.toString());

            this.setState({
                ready_to_check: false,
                waiting_for_tiling: true,
            })

            var that = this;
            var tiled_poem = []
            fetch(fetch_url).then(function(response) {
                return response.json();
            }).then(function(json) {
                tiled_poem = json.data;
                that.setState({
                    ready_to_tile: true,
                    waiting_for_tiling: false,
                    tiled_poem: tiled_poem,
                })
                return json;
            });
        } else {
            this.setState({
                ready_to_check: true,
                waiting_for_tiling: false,
                ready_to_tile: false,
            })
        }
    }

    setTiledPoem(tiled_poem) {
        this.setState({
            tiled_poem: tiled_poem,
        })
    }

    editPoem() {
        this.setState({
            enter_new_poem: true,
            ready_to_check: false,
            ready_to_tile: false,
        })
    }

    returnToCheck() {
        this.setState({
            enter_new_poem: false,
            ready_to_check: true,
            ready_to_tile: false,
        })
    }

	render() {
        // display new poem input if set to enter new poem
        let inputPoem;
        if (this.state.enter_new_poem) {
            inputPoem = <div>
						<div class="header">
						SONNET TILING
						</div>
						<div class = "container">
								<div class="instructions">
								<div class="instructions-title">
								INSTRUCTIONS
								</div>
								<div class="tool_definition">
								Hello! What is this tool? This tool creates polyomino puzzles out of Sonnets. The potential sizes are displayed on the next page, along with some other specifications. For each word in the sonnet, either the entirety of that word will be represented in a polomino puzzle piece, or none of it will be. That is, no word will be split between pieces.
								</div>
								<div class="how_to">
								Shakespearean Sonnets are generally broken into a six line and an eight line stanza. You can tile each of those separately with this tool. To use it, simply start by pasting your stanza of interest into this textbox to the right. Remember, there must be only 6 or 8 lines in this stanza. Specifications for the type of puzzle you would like to make will be made on the following page.
								</div>
								</div>
								<div class="textbox-outer">
								<div class="label-text">
		                Poem Text
										</div>

                <textarea
								class="textbox"
                cols="40"
                rows="20"
                id="poem_text"
                value={this.state.poem_text}
                onChange={() => this.setPoem()}
                ></textarea>
								<div class="button-class">
	                <button class='button' onClick={() => this.readyToCheck()}>
	                    Start Puzzling
	                </button>
									</div>
								</div>
								</div>
            </div>
        } else {
            inputPoem = ""
        }

        // display poem checker if ready to check
        let poemChecker;
        if (this.state.ready_to_check) {
            poemChecker = <div>
                    <PoemToCheck
                        lines={this.state.syllable_poem}
                        onChange={this.handlePoemEdit}
                        onWrong/>
                    </div>
        } else {
            poemChecker = ""
        }

        // display tiling menu if ready to check
        let tilingMenu;
        if (this.state.ready_to_check) {
            if (this.state.syllable_poem.length === 8) {
                tilingMenu = <div>
                        <EightLineMenu setOminoeTypes={this.setOminoeTypes}
                        ominoe_id={this.state.ominoe_id}
                        readyToTile={this.readyToTile}/>
                        <button onClick={this.editPoem}>Edit Poem Text</button>
                    </div>
            } else if(this.state.syllable_poem.length === 6) {
                tilingMenu = <div>
                        <SixLineMenu setOminoeTypes={this.setOminoeTypes}
                        readyToTile={this.readyToTile}
                        ominoe_id = {this.state.ominoe_id}/>
                        <button class="secondary-button" onClick={this.editPoem}>&#8592; Edit Poem Text</button>
                    </div>
            }
        }

        // display tiled puzzle if ready to tile
        let puzzleDisplay;
        if (this.state.ready_to_tile) {
            puzzleDisplay = <div>
                    <AllPuzzles syllable_poem={this.state.syllable_poem}
                    tiled_poem={this.state.tiled_poem}/>
                    <button class="secondary-button" onClick={this.editPoem}> &#8592; Edit Poem Text</button>
                    <button class="secondary-button" onClick={this.returnToCheck}>&#8592; Edit Poem Syllables</button>
                </div>
        } else {
            puzzleDisplay = ""
        }

        let loadingScreen;
        if (this.state.waiting_for_tiling) {
            loadingScreen = <div>Loading your tiling
                <div class="loader"></div>
            </div>
        } else {
            loadingScreen = ""
        }

		return (
			<div>
                {inputPoem}
                <div>
                    {poemChecker}
                    {tilingMenu}
                </div>
                <div>
                    {loadingScreen}
                    {puzzleDisplay}
                </div>
            </div>
		);
	}
}

export default PoemInput;
