import React, { Component } from "react";
import { Table } from "reactstrap";
import NewRecommendationModal from "./RecommendationModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class RecommendationList extends Component {
  render() {
    const recommendations = this.props.recommendations;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Recommendation</th>
            <th>Team</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!recommendations || recommendations.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, nothing here yet</b>
              </td>
            </tr>
          ) : (
            recommendations.map(recommendation => (
              <tr key={recommendation.id}>
                <td>{recommendation.recommendation_headline}</td>
                <td>{recommendation.team_name}</td>
                <td>{recommendation.status}</td>
                <td align="center">
                  <NewRecommendationModal
                    create={false}
                    recommendation={recommendation}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    id={recommendation.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default RecommendationList;