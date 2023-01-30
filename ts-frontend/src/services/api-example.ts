import axios from 'axios';

const API_BASE_URL = 'https://httpbin.org';

const getApiAxiosInstance = () => axios.create({ baseURL: API_BASE_URL });

export type ApiResponse = {
  args: { [key: string]: string }
  headers: { [key: string]: string }
  origin: string
  url: string
}

export const getApiResponse = async (): Promise<ApiResponse | false> => {
  try {
    const response = await getApiAxiosInstance().get('/get');
    return response.data;
  } catch (e: unknown) {
    console.log('Error while fetching api response', e);
    return false;
  }
};
