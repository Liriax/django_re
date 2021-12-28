export default function RecommendationDetails(props) {
    const { recommendation } = props
    return (
        <div>{JSON.stringify(recommendation)}</div>
    )
}