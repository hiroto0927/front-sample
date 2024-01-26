import UsersManager from "@/components/domain/users/users-manager";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <UsersManager />
    </main>
  );
}
