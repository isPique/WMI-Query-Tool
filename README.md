# INSTALLATION

```shell
pip install -r requirements.txt
```

# About Script
* This script provides a interface to explore and access various aspects of your system, making it easy to retrieve details about hardware, software, and other system parameters.

* Please make sure that the `queries.json` file is in the same directory where the current code is running.

# Notice

* This code contains only 50 of the **WMI classes**. If you want to find out more, [see.](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)

* ![terminal](https://github.com/isPique/WMI-Query-Tool/assets/139041426/2046eee3-6180-4be7-8cd2-e2ecebeeb352)

# Here's a breakdown of what information the code retrieves:
**_1- Win32_Account:_**

- This class represents user accounts on a Windows system. It contains information about user account settings, such as username, domain, and various properties related to the account.

**_2- Win32_Bios:_**

- This class provides information about the computer's BIOS (Basic Input/Output System). It includes details about the BIOS version, manufacturer, and other related information.

**_3- Win32_CDROMDrive:_**

- Win32_CDROMDrive represents CD/DVD-ROM drives on the system. It provides information about the installed CD/DVD drives, such as their type, capabilities, and media access properties.

**_4- Win32_ComputerSystem:_**

- This class contains information about the computer system, including its hardware specifications, operating system details, and network-related properties.

**_5- Win32_ComputerSystemProduct:_**

- Win32_ComputerSystemProduct provides information about the computer system's product details, such as the manufacturer, model, and version.

**_6- Win32_DiskDrive:_**

- This class represents physical disk drives on the system. It contains details about the hard drives, solid-state drives, or other storage devices, including capacity, model, and more.

**_7- Win32_EncryptedFile:_**

- Win32_EncryptedFile deals with files that are encrypted using Windows' file encryption system. It provides information about these encrypted files and their attributes.

**_8- Win32_EncryptedVolume:_**

- This class represents encrypted disk volumes or drives on the system, typically encrypted using BitLocker or a similar technology. It includes information about encryption status and related properties.

**_9- Win32_EncryptionMethod:_**

- Win32_EncryptionMethod describes encryption methods and algorithms available on the system. It provides details about the encryption techniques supported by the operating system.

**_10- Win32_EncryptionProvider:_**
 - This class deals with encryption providers that are installed on the system. It includes information about cryptographic providers used for encryption and decryption.

**_11- Win32_LockSetting:_**
 - Win32_LockSetting provides information about the lock settings on the system, including screen lock and password policies.

**_12- Win32_LogonSession:_**
 - This class deals with user logon sessions on the system. It contains information about active logon sessions, including user and domain details.

**_13- Win32_LogicalDisk:_**
 - This class represents logical disk volumes on the system, such as drive C: or D:. It provides information about these volumes, including size, free space, and file system type.

**_14- Win32_LogicalFileAccess:_**
 - This class represents file access permissions and settings for files on the system. It provides information about file access controls and permissions.

**_15- Win32_NetworkAdapter:_**
 - Win32_NetworkAdapter represents network adapters (network interface cards) on the system. It contains details about network hardware, including MAC addresses and connection status.

**_16- Win32_NetworkAdapterConfiguration:_**
 - This class provides configuration details for network adapters, including IP addresses, DNS settings, and other network-related parameters.

**_17- Win32_NetworkLoginProfile:_**
 - Win32_NetworkLoginProfile contains information about network login profiles, including details about users who have logged into the network.

**_18- Win32_NTDomain:_**
 - This class represents Windows NT domains and contains information about domain settings and properties.

**_19- Win32_NTDomainTrust:_**
 - Win32_NTDomainTrust provides information about trust relationships between Windows NT domains. It describes how domains are connected and trust each other.

**_20- Win32_NTEventLog:_**
 - This class deals with Windows NT event logs and provides information about event log properties, such as size and maximum log size.

**_21- Win32_NTLogEvent:_**
 - Win32_NTLogEvent represents log events in Windows NT event logs. It contains information about specific events recorded in the logs.

**_22- Win32_NTLogEventFile:_**
 - This class provides information about event log files in Windows NT, including their size and location.

**_23- Win32_OperatingSystem:_**
 - Win32_OperatingSystem contains information about the operating system, including version, build, and various system-related properties.

**_24- Win32_PhysicalMemory:_**
 - This class represents physical memory modules (RAM) installed in the computer. It provides details about memory capacity, type, and other memory-related attributes.

**_25- Win32_PortConnector:_**
 - Win32_PortConnector deals with physical port connectors on the computer, such as USB or serial ports. It includes information about the ports available on the system.

**_26- Win32_PnPEntity:_**
 - Win32_PnPEntity provides information about Plug and Play entities on the system, including devices and drivers.

**_27- Win32_PowerManagementEvent:_**
 - This class represents power management events on the system, including events related to power state changes.

**_28- Win32_Process:_**
 - Win32_Process deals with running processes on the system. It contains information about running applications and system processes.

**_29- Win32_Processor:_**
 - This class provides details about the processors (CPU) installed in the computer, including processor type, speed, and number of cores.

**_30- Win32_Product:_**
 - Win32_Product deals with installed software products on the system. It provides information about installed applications and their versions.

**_31- Win32_RecoveryConfig:_**
 - Win32_RecoveryConfig contains information about system recovery settings and configurations.

**_32- Win32_ScheduledJob:_**
 - This class represents scheduled tasks or jobs on the system. It includes information about tasks scheduled to run at specific times or events.

**_33- Win32_SecurityDescriptor:_**
 - Win32_SecurityDescriptor deals with security descriptors on the system, including access control lists (ACLs) and security settings for objects.

**_34- Win32_SecurityDescriptorHelper:_**
 - This class provides helper functions and information related to security descriptors and access control settings.

**_35- Win32_SecuritySetting:_**
 - Win32_SecuritySetting represents security settings on the system, including group policies and security options.

**_36- Win32_SecuritySettingOfLogicalFile:_**
 - This class provides security settings specific to logical files, including file access permissions and security options.

**_37- Win32_Service:_**
 - Win32_Service represents system services on the computer. It contains information about installed services, their status, and startup type.

**_38- Win32_ServiceControl:_**
 - This class deals with service control operations, including starting, stopping, and managing services on the system.

**_39- Win32_ShadowCopy:_**
 - Win32_ShadowCopy provides information about shadow copies, which are used for backup and recovery purposes.

**_40- Win32_SoftwareFeature:_**
 - This class deals with software features and components installed on the system, such as Windows features and roles.

**_41- Win32_StartupCommand:_**
 - Win32_StartupCommand represents programs and commands that are set to run at system startup. It includes information about startup applications.

**_42- Win32_SystemAccount:_**
 - This class represents system accounts and includes information about built-in and system-related accounts.

**_43- Win32_SystemDriver:_**
 - Win32_SystemDriver provides information about system drivers installed on the system, including driver details and status.

**_44- Win32_TokenGroups:_**
 - This class represents token groups in the system, including security groups and their associated properties.

**_45- Win32_UserAccount:_**
 - Win32_UserAccount represents user accounts on the system. It includes information about user properties, group memberships, and more.

**_46- Win32_UserProfile:_**
 - This class provides information about user profiles on the system, including profile paths and other user-specific settings.

**_47- Win32_Win32_PhysicalMemory:_**
 - This class seems to have a redundant name and may not exist in standard WMI classes. It may be a duplicate or incorrect listing.

**_48- Win32_Win32_PhysicalMemoryArray:_**
 - This class might be related to the physical memory arrays on the system, possibly in the context of server hardware configurations.

**_49- Win32_Win32_PhysicalMemoryLocation:_**
 - This class could represent the physical location information for memory modules in the system, indicating where each module is installed.

**_50- Win32_Win32_PhysicalMemorySpeed:_**
 - This class may provide information about the speed or clock frequency of the physical memory modules in the computer.
