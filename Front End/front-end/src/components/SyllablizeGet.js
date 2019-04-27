import React, {Component} from 'react';

class SyllablizeGet extends Component {
    constructor(props) {
		super(props);
    };

    componentDidMount() {
        console.log("component did mount")
        var request_string = ""
        for (var line in this.props.poem_lines) {
            request_string = request_string.concat("/");
            request_string = request_string.concat(this.props.poem_lines[line])
        }

        var fetch_url = "http://localhost:5000/api/poem-syllable?poem=";
        fetch_url = fetch_url.concat(request_string);

        var that = this;
        this.props.setSyllablePoem(request_string);
        fetch(fetch_url).then(function(response) {
            return response.json();
        }).then(function(json) {
            console.log(json)
            console.log(that.props)
            that.props.setSyllablePoem(json.data);
            return json;
        });
    }

    render() {
        return("");
    }
}

export default SyllablizeGet;

