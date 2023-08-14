import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await axios.post(`${API_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const getEstimate = async (filamentType, infillPercentage) => {
  const response = await axios.get(`${API_URL}/estimate`, {
    params: {
      filament_type: filamentType,
      infill_percentage: infillPercentage,
    },
  });
  return response.data;
};