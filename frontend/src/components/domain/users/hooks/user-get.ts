import useGetRequest from "@/hooks/get-request";
import { TPropsUser } from "../types/user";

export default function useGetUsers() {
  const { data, isLoading, error, mutate } =
    useGetRequest<TPropsUser[]>("/api/users");

  return { data, isLoading, error, mutate };
}
