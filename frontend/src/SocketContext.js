import React, { createContext, useContext, useEffect, useState } from "react";
import io from "socket.io-client";

const SocketContext = createContext();

export const useSocket = () => {
  return useContext(SocketContext);
};

export const SocketProvider = ({ children }) => {
  const [socket, setSocket] = useState(null);
  const [sid, setSid] = useState(null);

  useEffect(() => {
    const newSocket = io("http://localhost:8080", { transports: ["websocket"] });

    newSocket.on("connect", () => {
      setSid(newSocket.id);
      console.log("Socket connected:", newSocket.id);
    });

    newSocket.on("disconnect", () => {
      console.log("Socket disconnected");
    });

    setSocket(newSocket);

    // Clean up the socket when the component unmounts
    return () => {
      newSocket.disconnect();
    };
  }, []);

  return (
    <SocketContext.Provider value={{ socket, sid }}>
      {children}
    </SocketContext.Provider>
  );
};
