Name:		iproute
Version:	5.5.0
Release:	2
Summary:	Linux network configuration utilities
License:	GPLv2+ and Public Domain
URL:		https://kernel.org/pub/linux/utils/net/iproute2/
Source0:	https://mirrors.edge.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

Patch1:         bugfix-iproute2-3.10.0-fix-maddr-show.patch         
Patch2:         bugfix-iproute2-change-proc-to-ipnetnsproc-which-is-private.patch

Patch9002:	feature-iproute-limit-operation-ip-netns-del.patch
Patch9003:	feature-iproute-add-support-for-ipvlan-l2e-mode.patch
Patch9004:	feature-peer_notify_delay-renamed-to-peer_notif_delay.patch
Patch9005:	bugfix-iproute-support-assume-default-route.patch

BuildRequires:	gcc bison elfutils-libelf-devel flex iptables-devel libcap-devel
BuildRequires:  libdb-devel libmnl-devel libselinux-devel pkgconfig git

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
export LIBDIR='{_libdir}'
export IPT_LIB_DIR='/%{_lib}/xtables'
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
%doc README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%{_libdir}/tc/*
%{_datadir}/bash-completion/completions/tc

%files         devel
%defattr(-,root,root)
%license COPYING
%{_libdir}/libnetlink.a
%{_includedir}/*

%files         help
%defattr(-,root,root)
%doc README
%{_mandir}/*

%changelog
* Tue Sep 25 2020 zhouyihang <zhouyihang3@huawei.com> - 5.5.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:fix get_tc_lib err

* Fri Apr 17 2020 liaichun<liaichun@huawei.com> - 5.5.0-1
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:update to 5.5.0-1

* Sat Mar 21 2020 liaichun<liaichun@huawei.com> - 5.4.0-6
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:fix some err information

* Wed Mar 4 2020 liuzhikang<liuzhikang3@huawei.com> - 5.4.0-5
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:update patch

* Wed Mar 4 2020 wangli <wangli221@huawei.com> - 5.4.0-4
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:peer_notify_delay renamed to peer_notif_delay

* Mon Mar 2 2020 liuzhikang<liuzhikang3@huawei.com> - 5.4.0-3
- Type:bugfix
- ID:NA
- SUG:restart
- DESC: update patch

* Mon Jan 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.4.0-2
- fix maddr show and change proc to ipnetnsproc

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.4.0-1
- update to 5.4.0

* Fri Oct 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add the bugfix about iproute

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-1
- Package init
