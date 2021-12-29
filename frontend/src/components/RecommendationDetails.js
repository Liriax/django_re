import { Button } from "@mui/material";

export default function RecommendationDetails(props) {
  const { recommendation, onClose } = props;
  return (
    <div>
      <Button onClick={onClose}>close</Button>
      <div>{JSON.stringify(recommendation)}</div>
    </div>
  );
}
