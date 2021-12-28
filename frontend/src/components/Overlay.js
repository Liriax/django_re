import { Backdrop } from "@mui/material"

export default function Overlay(props) {
    const { children } = props

    return (
        <Backdrop sx={{ color: "#fff"}} open>
            {children}
        </Backdrop>
    )
}