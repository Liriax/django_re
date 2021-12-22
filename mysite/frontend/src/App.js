import React, { Component } from 'react';

class App extends Component {
  state = {
    recommendations: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8080/recommend/api/'); // fetching the data before the page loaded
      const recommendations = await res.json();
      console.log(recommendations);
      this.setState({
        recommendations
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.recommendations.map(item => (
          <div key={item.id}>
            <h1>{item.recommendation_body}</h1>
            <span>{item.team_name}</span>
            <p>{item.created_at}</p>
            <p>{item.status}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;