import { useState, createContext } from "react";
import { Routes, Route } from "react-router-dom";
import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from "@mui/material";
import Topbar from "./components/Topbar";
import Sidebar from "./components/Sidebar";
import Vault from "./pages/Vault";
import Favourites from "./pages/Favourites";
import Passwords from "./pages/Passwords";
import Cards from "./pages/Cards";
import Notes from "./pages/Notes";
import Folder from "./pages/Folder";

export const SidebarContext = createContext();

function App() {
  const [theme, colorMode] = useMode();
  const [menu, setMenu] = useState(true);
  const [drawerOpen, setDrawerOpen] = useState(menu);
  
  return (
    <ColorModeContext.Provider value={colorMode}>
    <ThemeProvider theme={theme}>
    <SidebarContext.Provider value={{menu, setMenu, drawerOpen, setDrawerOpen}}>
    <CssBaseline>
      <div className="App">
        <Topbar />
        <main className="main">
          <Sidebar />
          <Routes>
            <Route path="/" element={<Vault />} />
            <Route path="/favourites" element={<Favourites />} />
            <Route path="/passwords" element={<Passwords />} />
            <Route path="/cards" element={<Cards />} />
            <Route path="/notes" element={<Notes />} />
            <Route path="/folder" element={<Folder />} />
          </Routes>
        </main>
      </div>
    </CssBaseline> 
    </SidebarContext.Provider>
    </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
