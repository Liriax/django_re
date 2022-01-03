import { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Bar, RecommendationDetails, RecommendationList } from "../components";
import * as API from "../api";

export default function Home() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [recommendations, setRecommendations] = useState(null);
  const [recommendation, setRecommendation] = useState(null);

  const fetchRecommendations = async () => {
    try {
      const result = await API.recommendations.team(1);
      setRecommendations(result.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchRecommendations();
  }, []);

  const fetchRecommendation = useCallback(async () => {
    try {
      const result = await API.recommendations.recommendation(id);
      setRecommendation(result.data);
    } catch (error) {
      console.log(error);
    }
  }, [id]);

  useEffect(() => {
    if (id) {
      fetchRecommendation();
    } else {
      setRecommendation(null);
    }
  }, [id, fetchRecommendation, setRecommendation]);

  const handleClickRecommendation = (event, recommendation) => {
    navigate(`/recommendation/${recommendation.id}`);
  };

  const handleCloseRecommendation = () => {
    navigate("../");
  };

  const handleClickImplement = (id) => {
    try {
      API.recommendations.edit(id, { status: "implemented" });
    } catch (error) {
      console.log(error);
    }
  };

  const handleClickRejected = (id) => {
    try {
      API.recommendations.edit(id, { status: "rejected" });
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
                unapliccable: handleClickRejected,
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
