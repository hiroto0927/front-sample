import axios from "axios";
import { TPropsUpdateUser } from "../types/user";

export const updateUserRequest = (userId: number, data: TPropsUpdateUser) => {
  return axios.patch(`/api/users/${userId}`, data);
};
