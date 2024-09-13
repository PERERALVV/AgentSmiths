import React, { useEffect, useState } from "react";
import { GradientTextDiv } from "../../../styles/components/GradientText";
import {
  DownloadButton,
  RightHolderDiv,
  RightHolderImage,
} from "../../../styles/pages/ChatInterface";
import { useSocket } from "../../../SocketContext";

function ChatRightHolder() {
  const { socket, sid } = useSocket();
  const [isConnected, setIsConnected] = useState(false);
  const [isCodeReady, setIsCodeReady] = useState(false);

  useEffect(() => {
    if (!socket) {
      console.warn("Socket is not available from the context.");
      return;
    }

    const handleConnect = () => {
      setIsConnected(true);
      console.log("Socket connected in RightHolder: ", sid);
    };

    const handleDisconnect = () => {
      setIsConnected(false);
      console.log("Socket disconnected in RightHolder");
    };

    const handleCodeReady = () => {
      console.log("Starting to create the website");
      setIsCodeReady(true);
    };

    socket.on("connect", handleConnect);
    socket.on("disconnect", handleDisconnect);
    socket.on("code_ready", handleCodeReady);

    // Cleanup to avoid multiple listeners
    return () => {
      socket.off("connect", handleConnect);
      socket.off("disconnect", handleDisconnect);
      socket.off("code_ready", handleCodeReady);
    };
  }, [socket, sid]);

  const handleDownload = () => {
    console.log("Download button clicked");
    socket.emit("download_file");
    console.log("Download request sent");
  };

  return (
    <RightHolderDiv>
      <RightHolderImage src="RightHolder.gif" alt="Unprocessed Image" />
      {isCodeReady ? (
        <DownloadButton onClick={handleDownload}>
          Download Source Code
        </DownloadButton> // Render the download button when code is ready
      ) : (
        <GradientTextDiv>Building ...</GradientTextDiv>
      )}
    </RightHolderDiv>
  );
}

export default ChatRightHolder;
