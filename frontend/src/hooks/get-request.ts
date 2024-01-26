"use client";
import { fetcher } from "@/lib/fetch";
import useSWR from "swr";

function useGetRequest<T>(url: string | null) {
  const { data, error, isLoading, mutate } = useSWR(url, fetcher);
  return {
    data: data as T,
    isLoading,
    error,
    mutate,
  };
}

export default useGetRequest;
