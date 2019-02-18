import std.stdio;
import ddbus;

void main()
{
	Connection conn = connectToBus();
	PathIface obj = new PathIface(conn, "org.freedesktop.DBus","/org/freedesktop/DBus", "org.freedesktop.DBus");
	// call any method with any parameters and then convert the result to the right type.
	auto name = obj.GetNameOwner("org.freedesktop.DBus").to!string();
	writeln(name);
	// alternative method
	string name2 = obj.call!string("GetNameOwner","org.freedesktop.DBus");
	writeln(name2);
}