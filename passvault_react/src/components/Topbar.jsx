import { AppBar, Box, IconButton, Toolbar, Typography, useTheme } from "@mui/material";
import { useContext } from "react";
import { ColorModeContext, tokens } from "../theme";
import { SidebarContext } from "../App";
import styled from "@emotion/styled";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import { MenuOutlined } from "@mui/icons-material";
export default function Topbar() {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext);
  const StyledAppBar = styled(AppBar)({
    position:"sticky",
    display:"flex",
    color: colors.grey[100]
  })
  const StyledToolbar = styled(Toolbar)({
    diplay:"flex",
    justifyContent:"space-between",
    backgroundColor: colors.grey[900]
  })
  const StyledIconButton = styled(IconButton)({
    color:colors.grey[100]
  })

  const {setMenu, setDrawerOpen} = useContext(SidebarContext);
  const handleOnClickMenuButton = () => {
    setMenu(prev=>!prev)
    setDrawerOpen(prev=>!prev)
  }
  return (
    <StyledAppBar id="topbar">
      <StyledToolbar>
        <Box display="flex" alignItems="center" justifyContent="space-between" gap={3}>
          <StyledIconButton onClick={handleOnClickMenuButton}>
            <MenuOutlined />
          </StyledIconButton>
          <Typography variant="h1" component="logo">PassVault</Typography>
        </Box>
        <Box display="flex">
          <StyledIconButton onClick={colorMode.toggleColorMode}>
            {theme.palette.mode === "dark" ? <DarkModeOutlinedIcon /> : <LightModeOutlinedIcon />}
          </StyledIconButton>
          <StyledIconButton>
            <PersonOutlinedIcon />
          </StyledIconButton>
        </Box>
      </StyledToolbar>
    </StyledAppBar>
  );
};