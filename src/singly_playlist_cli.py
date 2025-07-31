class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_node = Node(title)
        if not self.head:  # Empty list
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to end
                current = current.next
            current.next = new_node
        print(f"\n🎵  Song added: {title}")

    def play_next(self):
        if not self.head:
            print("\n⚠️  No songs in the playlist.")
            return
        current_song = self.head.data
        self.head = self.head.next  # Move to next
        print("\n🎧 Now Playing:")
        print(f"   ────────────────────────────────")
        print(f"   ▶️  {current_song}")
        print(f"   ────────────────────────────────")

    def traverse(self):
        if not self.head:
            print("\n📂 Playlist is empty.")
            return
        current = self.head
        print("\n📂 Current Playlist:")
        print("   ────────────────────────────────")
        i = 1
        while current:
            print(f"   {i}. {current.data}")
            current = current.next
            i += 1
        print("   ────────────────────────────────")

# Menu-driven interaction
playlist = Playlist()

while True:
    print("\n=== 🎼 Playlist Manager ===")
    print("1️⃣  Add Song")
    print("2️⃣  Play Next")
    print("3️⃣  Show Playlist")
    print("4️⃣  Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter song title: ")
        playlist.add_song(title)
    elif choice == '2':
        playlist.play_next()
    elif choice == '3':
        playlist.traverse()
    elif choice == '4':
        print("\n👋 Exiting Playlist. See you soon!")
        break
    else:
        print("\n❌ Invalid choice, try again.")
