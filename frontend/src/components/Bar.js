import { useState } from "react"
import { AppBar, Box, Toolbar, IconButton, Typography, Menu, Container, Avatar, Button, Tooltip, MenuItem } from "@mui/material"
import { Menu as MenuIcon } from "@mui/icons-material"

const pages = ["Page"]
const settings = ["Setting"]

export default function Bar() {
	const [openNavigation, setOpenNavigation] = useState(false)
	const [openSettings, setOpenSettings] = useState(false)

	const toggleNavigation = () => {
		setOpenNavigation(open => !open)
	}

	const toggleSettings = () => {
		setOpenSettings(open => !open)
	}

	return (
		<AppBar position="static">
			<Container maxWidth="xl">
				<Toolbar disableGutters>
					<Typography noWrap variant="h6" component="div" sx={{mr: 2, display: {xs: "none", md: "flex"}}}>
                        <img width="50%" src="logo.png" alt="Logo" />
					</Typography>
					<Box sx={{flexGrow: 1, display: {xs: "flex", md: "none"}}}>
						<IconButton onClick={toggleNavigation} size="large" aria-haspopup="true" color="inherit">
							<MenuIcon />
						</IconButton>
						<Menu keepMounted open={openNavigation} onClose={toggleNavigation} anchorOrigin={{vertical: "bottom", horizontal: "left"}} transformOrigin={{vertical: "top", horizontal: "left"}} sx={{display: {xs: "block", md: "none"}}}>
							{pages.map((page) => (
								<MenuItem key={page} onClick={toggleNavigation}>
									<Typography textAlign="center">{page}</Typography>
								</MenuItem>
							))}
						</Menu>
					</Box>

					<Typography noWrap variant="h6" component="div" sx={{flexGrow: 1, display: {xs: "flex", md: "none"}}}>
                        <img width="30%" src="logo.png" alt="Logo" />
					</Typography>
					<Box sx={{flexGrow: 1, display: {xs: "none", md: "flex"}}}>
						{pages.map((page) => (
							<Button key={page} onClick={toggleNavigation} sx={{my: 2, color: "white", display: "block"}}>
								{page}
							</Button>
						))}
					</Box>

					<Box sx={{flexGrow: 0}}>
						<Tooltip title="Open settings">
							<IconButton onClick={toggleSettings} sx={{p: 0}}>
								<Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
							</IconButton>
						</Tooltip>
						<Menu keepMounted open={openSettings} onClose={toggleSettings} anchorOrigin={{vertical: "top", horizontal: "right"}} transformOrigin={{vertical: "top", horizontal: "right"}} sx={{mt: "45px"}} >
							{settings.map((setting) => (
								<MenuItem key={setting} onClick={toggleSettings}>
									<Typography textAlign="center">{setting}</Typography>
								</MenuItem>
							))}
						</Menu>
					</Box>
				</Toolbar>
			</Container>
		</AppBar>
	)
}