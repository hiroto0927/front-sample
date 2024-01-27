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
            name: (
              <input
                type="text"
                className="outline-none"
                onBlur={(e) => {
                  const value = e.target.value;
                  const isValid =
                    /^[a-zA-Z\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]*$/.test(
                      value
                    );
                  if (!isValid) {
                    e.target.value = user.name;
                    return alert("無効な文字が入力されています");
                  }

                  if (value.length > 20) {
                    e.target.value = user.name;
                    return alert("20文字以内で入力してください");
                  }

                  if (value.length < 1) {
                    e.target.value = user.name;
                    return alert("1文字以上入力してください");
                  }

                  updateUserRequest(user.id, {
                    name: e.target.value,
                  }).then(() => mutate());
                }}
                onKeyUp={(e) => {
                  if (e.key === "Enter") {
                    (e.target as HTMLInputElement).blur();
                  }
                }}
                defaultValue={user.name}
              />
            ),
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
