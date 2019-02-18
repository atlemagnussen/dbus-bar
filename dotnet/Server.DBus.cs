using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using Tmds.DBus;

[assembly: InternalsVisibleTo(Tmds.DBus.Connection.DynamicAssemblyName)]
namespace Server.DBus
{
    [DBusInterface("org.freedesktop.ReserveDevice1")]
    interface IReserveDevice1 : IDBusObject
    {
        Task<bool> RequestReleaseAsync(int Priority);
        Task<T> GetAsync<T>(string prop);
        Task<ReserveDevice1Properties> GetAllAsync();
        Task SetAsync(string prop, object val);
        Task<IDisposable> WatchPropertiesAsync(Action<PropertyChanges> handler);
    }

    [Dictionary]
    class ReserveDevice1Properties
    {
        private int _Priority = default (int);
        public int Priority
        {
            get
            {
                return _Priority;
            }

            set
            {
                _Priority = (value);
            }
        }

        private string _ApplicationName = default (string);
        public string ApplicationName
        {
            get
            {
                return _ApplicationName;
            }

            set
            {
                _ApplicationName = (value);
            }
        }

        private string _ApplicationDeviceName = default (string);
        public string ApplicationDeviceName
        {
            get
            {
                return _ApplicationDeviceName;
            }

            set
            {
                _ApplicationDeviceName = (value);
            }
        }
    }

    static class ReserveDevice1Extensions
    {
        public static Task<int> GetPriorityAsync(this IReserveDevice1 o) => o.GetAsync<int>("Priority");
        public static Task<string> GetApplicationNameAsync(this IReserveDevice1 o) => o.GetAsync<string>("ApplicationName");
        public static Task<string> GetApplicationDeviceNameAsync(this IReserveDevice1 o) => o.GetAsync<string>("ApplicationDeviceName");
    }

    [DBusInterface("org.PulseAudio.ServerLookup1")]
    interface IServerLookup1 : IDBusObject
    {
        Task<T> GetAsync<T>(string prop);
        Task<ServerLookup1Properties> GetAllAsync();
        Task SetAsync(string prop, object val);
        Task<IDisposable> WatchPropertiesAsync(Action<PropertyChanges> handler);
    }

    [Dictionary]
    class ServerLookup1Properties
    {
        private string _Address = default (string);
        public string Address
        {
            get
            {
                return _Address;
            }

            set
            {
                _Address = (value);
            }
        }
    }

    static class ServerLookup1Extensions
    {
        public static Task<string> GetAddressAsync(this IServerLookup1 o) => o.GetAsync<string>("Address");
    }
}