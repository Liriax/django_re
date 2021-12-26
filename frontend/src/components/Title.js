import { PropTypes } from "prop-types"

export default function Title(props) {
    const style = () => {
        return {
            style: {
                color: props.color
            }
        }
    }

    return (
        <h1 onClick={props.onClick} {...style()}>
            {props.uppercase ? props.children?.toUpperCase() : props.children}
        </h1>
    )
}

Title.propTypes = {
    children: PropTypes.string,
    uppercase: PropTypes.bool,
    color: PropTypes.string,
    onClick: PropTypes.func
}