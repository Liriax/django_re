export default function RecommendationDetails(props) {
  const { recommendation, onClose } = props;
  return (
    <div>
      <button onClick={onClose}>close</button>
      <div>{JSON.stringify(recommendation)}</div>
    </div>
  );
}
