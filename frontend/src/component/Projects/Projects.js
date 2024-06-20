import React, { useEffect, useState } from 'react';
import { CircularProgress, Container, Typography } from '@material-ui/core';
import axios from 'axios';

const UserFile = ({ userId, fileName }) => {
  const [fileUrl, setFileUrl] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUserFile = async () => {
      try {
        const response = await axios.get(`/user/${userId}/file/${fileName}`, {
          responseType: 'blob',
        });
        const fileBlob = new Blob([response.data]);
        setFileUrl(URL.createObjectURL(fileBlob));
      } catch (error) {
        console.error('Error fetching file:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchUserFile();
  }, [userId, fileName]);

  if (loading) {
    return (
      <Container>
        <CircularProgress />
      </Container>
    );
  }

  return (
    <Container>
      {fileUrl ? (
        <a href={fileUrl} download>
          Download File
        </a>
      ) : (
        <Typography variant="body1">File not found</Typography>
      )}
    </Container>
  );
};

export default UserFile;
