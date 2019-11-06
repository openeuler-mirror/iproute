Name:		iproute
Version:	5.2.0
Release:	2
Summary:	Linux network configuration utilities
License:	GPLv2+ and Public Domain
URL:		https://kernel.org/pub/linux/utils/net/iproute2/
Source0:	https://mirrors.edge.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

BuildRequires:	gcc bison elfutils-libelf-devel flex iptables-devel libcap-devel
BuildRequires:  libdb-devel libmnl-devel libselinux-devel pkgconfig git

Patch9001:      bugfix-iproute2-3.10.0-fix-maddr-show.patch
Patch9002:      bugfix-iproute-support-assume-default-route.patch

Patch0001:      0001-Revert-ip6tunnel-fix-ip-6-show-change-dev-name-cmds.patch
Patch0002:      0002-ip-tunnel-warn-when-changing-IPv6-tunnel-without-tun.patch
Patch0003:      0003-ip-route-fix-json-formatting-for-metrics.patch
Patch0004:      0004-utils-move-parse_percent-to-tc_util.patch
Patch0005:      0005-tc-util-constrain-percentage-in-0-100-interval.patch
Patch0006:      0006-devlink-Change-devlink-health-dump-show-command-to-d.patch
Patch0007:      0007-devlink-Fix-binary-values-print.patch
Patch0008:      0008-devlink-Remove-enclosing-array-brackets-binary-print.patch
Patch0009:      0009-json-fix-backslash-escape-typo-in-jsonw_puts.patch

Patch9003:      bugfix-1001-iproute-change-proc-to-ipnetnsproc-which-is-private.patch
	
Provides:       /sbin/ip iproute-tc tc 
Obsoletes:      iproute-tc 

%description
Iproute2 is a collection of user-space utilities to set up networking
under Linux from the command-line. It can inspect and configure,
among other things: interface paramters, IP addresses, routing,
tunnels, bridges, packet transformations (IPsec, etc.), and Quality
of Service.

%package        devel
Summary:        Header files for iprout2
License:        GPLv2+
Provides:       iproute-static = %{version}-%{release}
Obsoletes:      iproute-static < %{version}-%{release}

%description    devel
Header files for iprout2

%package_help

%prep
%autosetup -n %{name}2-%{version} -p1 -S git

%build
%configure
%make_build

%install
export CONFDIR='%{_sysconfdir}/iproute2'
export SBINDIR='%{_sbindir}'
export LIBDIR='%{_libdir}'
export DOCDIR='%{_docdir}'

%make_install 

install -m 0755 -d %{buildroot}%{_includedir}
install -m 0644 include/libnetlink.h %{buildroot}%{_includedir}/libnetlink.h
install -m 0644 lib/libnetlink.a %{buildroot}%{_libdir}/libnetlink.a

%files
%defattr(-,root,root)
%license COPYING
%doc README.lnstat
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%{_libdir}/tc/*
%{_datadir}/bash-completion/completions/tc

%files         devel
%defattr(-,root,root)
%license COPYING
%{_libdir}/libnetlink.a
%{_includedir}/*
%{_datadir}/doc/examples

%files         help
%defattr(-,root,root)
%doc README README.distribution README.iproute2+tc
%{_mandir}/*

%changelog
* Fri Oct 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add the bugfix about iproute

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-1
- Package init
