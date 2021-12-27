import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import RecommendationList from "./RecommendationList";
import NewRecommendationModal from "./RecommendationModal";
import { Bar } from "../components"

import axios from "axios";

const API_URL  = "http://127.0.0.1:8080/recommend/api/";

class Home extends Component {
  state = {
    recommendations: []
  };

  componentDidMount() {
    this.resetState();
  }

  getRecommendations = () => {
    axios.get(API_URL).then(res => this.setState({ recommendations: res.data }));
  };

  resetState = () => {
    this.getRecommendations();
  };

  render() {
    return (
      <>
      <Bar/>
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <RecommendationList
              recommendations={this.state.recommendations}
              resetState={this.resetState}
              />
          </Col>
        </Row>
      </Container>
      </>
    );
  }
}

export default Home;