"use client";

import BaseTable from "@/components/ui/table/base-table";
import useGetUsers from "./hooks/user-get";
import ToggleSwitch from "@/components/ui/form/toggle-switch";
import { updateUserRequest } from "./lib/user-request";

export default function UsersManager() {
  const { data, isLoading, error, mutate } = useGetUsers();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>{error.message}</div>;

  return (
    <div className="p-10 max-h-[80vh]">
      <BaseTable
        cols={[
          { key: "id", label: "ID" },
          { key: "name", label: "Name" },
          { key: "is_admin", label: "権限" },
          { key: "is_active", label: "ステータス" },
          { key: "is_notice", label: "通知" },
        ]}
        rows={
          data?.map((user) => ({
            id: user.id,
            name: user.name,
            is_admin: (
              <ToggleSwitch
                isCheck={user.is_admin}
                onChange={(e) => {
                  updateUserRequest(user.id, {
                    is_admin: e.target.checked,
                  }).then(() => mutate());
                }}
              />
            ),
            is_active: (
              <ToggleSwitch
                isCheck={user.is_active}
                onChange={(e) => {
                  updateUserRequest(user.id, {
                    is_active: e.target.checked,
                  }).then(() => mutate());
                }}
              />
            ),
            is_notice: (
              <ToggleSwitch
                isCheck={user.is_notice}
                onChange={(e) => {
                  updateUserRequest(user.id, {
                    is_notice: e.target.checked,
                  }).then(() => mutate());
                }}
              />
            ),
            onClickCell: () => {},
          })) ?? []
        }
      />
    </div>
  );
}
