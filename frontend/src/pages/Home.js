import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Bar, RecommendationDetails, RecommendationList } from "../components";
import * as API from "../api";

export default function Home() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [recommendations, setRecommendations] = useState(null);
  const [recommendation, setRecommendation] = useState(null);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  useEffect(() => {
    if (id) {
      fetchRecommendation();
    } else {
      setRecommendation(null);
    }
  }, [id]);

  const fetchRecommendations = async () => {
    try {
      const result = await API.recommendations.team(1);
      setRecommendations(result.data);
    } catch (error) {
      console.log(error);
    }
  };

  const fetchRecommendation = async () => {
    try {
      const result = await API.recommendations.recommendation(id);
      setRecommendation(result.data);
    } catch (error) {
      console.log(error);
    }
  };

  const handleClickRecommendation = (event, recommendation) => {
    navigate(`/recommendation/${recommendation.id}`);
  };

  const handleCloseRecommendation = () => {
    navigate("../");
  };

  const handleClickImplement = (id) => {
    try {
      API.recommendations.edit(id, { status: "REJECTED" });
    } catch (error) {
      console.log(error);
    }
  };

  const handleClickInapplicable = (id) => {
    try {
      API.recommendations.edit(id, { status: "REJECTED" });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <Bar />
      {recommendations ? (
        <>
          <RecommendationList
            recommendations={recommendations}
            onClick={{ recommendation: handleClickRecommendation }}
          />
          {recommendation && (
            <RecommendationDetails
              recommendation={recommendation}
              onClick={{
                implement: handleClickImplement,
                unapliccable: handleClickInapplicable,
                close: handleCloseRecommendation,
              }}
            />
          )}
        </>
      ) : (
        "Loading"
      )}
    </>
  );
}
