import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

const API_URL  = "http://127.0.0.1:8080/recommend/api/";
class NewRecommendationForm extends React.Component {
  state = {
    id: 1, 
    recommendation: 0, 
    team: 0, 
    created_at: "", 
    status: "",
    recommendation_headline: "",
    team_name:"",
  };

  componentDidMount() {
    if (this.props.recommendation) {
      const { id, recommendation, team, created_at, status,recommendation_headline,team_name } = this.props.recommendation;
      this.setState({ id, recommendation, team, created_at, status,recommendation_headline,team_name });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  // createRecommendation = e => {
  //   e.preventDefault();
  //   axios.post(API_URL, this.state).then(() => {
  //     this.props.resetState();
  //     this.props.toggle();
  //   });
  // };

  editRecommendation = e => {
    e.preventDefault();
    // PUT to the django api
    axios.put(API_URL + this.state.id, this.state).then(() => {
      console.log(this.state);
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.editRecommendation}>
        {/* <FormGroup>
          <Label for="recommendation_headline">Recommendation:</Label>
          <Input
            type="text"
            name="recommendation_headline"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.recommendation_headline)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="team_name">Team:</Label>
          <Input
            type="text"
            name="team_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.team_name)}
          />
        </FormGroup> */}
        <FormGroup>
          <Label for="status">Status:</Label>
          <Input
            type="text"
            name="status"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.status)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewRecommendationForm;